#!/bin/bash

function main() {
	local file="$1"

	if [ -z "$file" ]; then
		echo -e "\e[31mUsage: $0 <file>\e[0m"
		exit 1
	fi

	fileName=$(echo $file | grep -oP '(?<=markdown/).*(?=\.md)')

	body=$(pandoc $file)

	if [ $? -ne 0 ]; then
		echo -e "\e[31mThere was an error generating the html content from ${file}.\e[0m"
		exit 1
	fi

	htmlTemplate=$(cat blog-template.html)

	htmlContent=$(awk -v title="$fileName" -v body="$body" '{gsub(/\$title\$/, title); gsub(/\$body\$/, body); print}' <<< "$htmlTemplate")
	htmlContent=$(echo "$htmlContent" | sed 's/\$body\$/\&/g')

	htmlContent=$(echo "$htmlContent" | sed -E 's/(<div class="sourceCode" id="([^"]+)">)/\1<button class="button-to-clipboard" onclick="copyToClipboard('\''#\2 code'\''); changeButtonColor(this);">Copy<\/button>/g')

	htmlContent=$(echo "$htmlContent" | sed 's/class="sourceCode /class="source-code-/g')
	htmlContent=$(echo "$htmlContent" | sed 's/class="sourceCode/class="source-code/g')

	echo "$htmlContent" > html/${fileName}.html

	if [ $? -eq 0 ]; then
		echo -e "\e[32mThe file ${fileName}.html was generated successfully.\e[0m"
	else
		echo -e "\e[31mThere was an error generating the file ${fileName}.html.\e[0m"
		exit 1
	fi
}

main $@
