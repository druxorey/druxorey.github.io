import"./main-C862Lgn9.js";import"./main-BfJ2_Rrr.js";const b=[{id:"fundamentos-de-comunicacion-y-topologias-de-red",title:"#01 - Fundamentos de Comunicación y Topologías de Red",rawTitle:"Fundamentos de Comunicación y Topologías de Red",slug:"fundamentos-de-comunicacion-y-topologias-de-red.html",subject:"Comunicación de datos",order:1,orderBadge:"#01",summary:"La comunicación de datos permite el intercambio de información digital mediante protocolos normalizados que gestionan la transmisión, el enrutamiento y la integridad de los paquetes. Mediante el uso de conmutación de paquetes, diversas topologías de red y una jerarquía de ISP, los sistemas garantizan la conectividad global, optimizando el rendimiento a través de métricas críticas como latencia, ancho de banda y QoS.",tags:["académico"]},{id:"modelos-en-capas-y-protocolos-de-red",title:"#02 - Modelos en Capas y Protocolos de Red",rawTitle:"Modelos en Capas y Protocolos de Red",slug:"modelos-en-capas-y-protocolos-de-red.html",subject:"Comunicación de datos",order:2,orderBadge:"#02",summary:"Los modelos en capas estructuran la comunicación de red mediante jerarquías funcionales que facilitan la interoperabilidad y escalabilidad de sistemas heterogéneos. Mientras el modelo OSI actúa como marco conceptual, la pila TCP/IP constituye la arquitectura práctica de Internet, gestionando el encapsulamiento de datos, el direccionamiento IP y los mecanismos de transporte confiable o eficiente, optimizados actualmente mediante protocolos modernos como QUIC.",tags:["académico"]},{id:"senales-y-analisis-espectral",title:"#03 - Señales y Análisis Espectral",rawTitle:"Señales y Análisis Espectral",slug:"senales-y-analisis-espectral.html",subject:"Comunicación de datos",order:3,orderBadge:"#03",summary:"Las señales electromagnéticas constituyen la base física de la comunicación, permitiendo la transmisión de información mediante variaciones en el dominio del tiempo y la frecuencia. El análisis espectral, fundamentado en la serie de Fourier, facilita la gestión del ancho de banda y la propagación en el espacio, considerando factores críticos como las zonas de Fresnel y el efecto Doppler en sistemas inalámbricos.",tags:["académico"]}];function E(){const u=document.getElementById("notesContainer"),c=document.getElementById("notesSubjectsList"),r=document.getElementById("notesTagsContainer"),p=document.getElementById("notesSearchInput"),f=document.getElementById("notesCount");if(!u)return;const l=new Map;b.forEach(e=>{const t=l.get(e.subject)||0;l.set(e.subject,t+1)});let n="all",y="";const v=`
		<svg class="notes-folder-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
			<path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
		</svg>
	`;function h(){if(!c)return;c.innerHTML="";const e=document.createElement("li"),t=document.createElement("button");t.className=`notes-sidebar-item ${n==="all"?"active":""}`,t.setAttribute("type","button"),t.innerHTML=`
			<span class="notes-sidebar-item-left">
				${v}
				<span class="notes-sidebar-item-name">Todas las materias</span>
			</span>
			<span class="notes-sidebar-item-count">${b.length}</span>
		`,t.addEventListener("click",()=>{n="all",d(),i()}),e.appendChild(t),c.appendChild(e),Array.from(l.keys()).sort((s,o)=>s.localeCompare(o)).forEach(s=>{const o=l.get(s)||0,g=document.createElement("li"),m=document.createElement("button");m.className=`notes-sidebar-item ${n===s?"active":""}`,m.setAttribute("type","button"),m.innerHTML=`
				<span class="notes-sidebar-item-left">
					${v}
					<span class="notes-sidebar-item-name">${s}</span>
				</span>
				<span class="notes-sidebar-item-count">${o}</span>
			`,m.addEventListener("click",()=>{n=s,d(),i()}),g.appendChild(m),c.appendChild(g)})}function C(){if(!r)return;r.innerHTML="";const e=document.createElement("button");e.className=`tag tag-interactive ${n==="all"?"active":""}`,e.textContent="Todas",e.setAttribute("type","button"),e.addEventListener("click",()=>{n="all",d(),i()}),r.appendChild(e),Array.from(l.keys()).sort().forEach(t=>{const a=document.createElement("button");a.className=`tag tag-interactive ${n===t?"active":""}`,a.textContent=t,a.setAttribute("type","button"),a.addEventListener("click",()=>{n=n===t?"all":t,d(),i()}),r.appendChild(a)})}function d(){c&&c.querySelectorAll(".notes-sidebar-item").forEach(t=>{var o;const a=t.querySelector(".notes-sidebar-item-name"),s=a?(o=a.textContent)==null?void 0:o.trim():"";n==="all"&&s==="Todas las materias"||s===n?t.classList.add("active"):t.classList.remove("active")}),r&&r.querySelectorAll(".tag").forEach(t=>{var s;const a=(s=t.textContent)==null?void 0:s.trim();n==="all"&&a==="Todas"||a===n?t.classList.add("active"):t.classList.remove("active")})}function i(){if(!u)return;const e=y.trim().toLowerCase(),t=b.filter(a=>{const s=n==="all"||a.subject===n,o=!e||a.title.toLowerCase().includes(e)||a.rawTitle.toLowerCase().includes(e)||a.summary.toLowerCase().includes(e)||a.subject.toLowerCase().includes(e)||a.tags.some(g=>g.toLowerCase().includes(e));return s&&o});if(f){const a=n==="all"?"":` · ${n}`;f.textContent=`Mostrando ${t.length} de ${b.length} notas${a}`}if(t.length===0){u.innerHTML=`
				<div class="card blog-empty-card">
					<p class="blog-empty-text">No se encontraron apuntes que coincidan con la búsqueda.</p>
					<button id="clearNotesSearchBtn" class="btn btn-secondary btn-sm" type="button">Limpiar filtros</button>
				</div>
			`;const a=document.getElementById("clearNotesSearchBtn");a&&a.addEventListener("click",()=>{n="all",y="",p&&(p.value=""),d(),i()});return}u.innerHTML=t.map(L).join("")}function L(e){const t=e.tags.map(a=>`<span class="tag">#${a}</span>`).join(" ");return`
			<a href="./notes/${e.slug}" class="card card-interactive note-card-row" aria-label="${e.title}">
				<div class="note-card-body">
					<div class="note-card-header">
						<div class="note-card-badges">
							<span class="note-badge-order">${e.orderBadge}</span>
							<span class="note-badge-subject">${e.subject}</span>
						</div>
					</div>

					<h2 class="note-card-title">
						${e.title}
					</h2>

					<p class="note-card-summary">
						${e.summary}
					</p>

					<div class="note-card-tags">
						${t}
					</div>
				</div>
			</a>
		`}p&&p.addEventListener("input",e=>{y=e.target.value,i()}),h(),C(),i()}document.addEventListener("DOMContentLoaded",E);
