function selectBlogCategory(id) {
    var categories = ['cozy-guides', 'learning'];

    categories.forEach(category => {
		var selector = document.getElementById('selector-' + category);
        var div = document.getElementById(category);
        div.style.display = 'none';
		selector.style.color = 'var(--color-foreground-1)';
    });

    var selectedDiv = document.getElementById(id);
    var selectedSelector = document.getElementById('selector-' + id);
    selectedDiv.style.display = 'flex';
    selectedSelector.style.color = 'var(--color-purple-2)';
}
