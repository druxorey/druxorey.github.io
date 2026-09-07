import"./main-C862Lgn9.js";document.addEventListener("DOMContentLoaded",()=>{const i=document.getElementById("contactForm"),e=document.getElementById("formStatus"),t=document.getElementById("copyEmailBtn"),s="druxorey@gmail.com";t&&t.addEventListener("click",async()=>{try{await navigator.clipboard.writeText(s);const o=t.innerHTML;t.innerHTML=`
					<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-green">
						<polyline points="20 6 9 17 4 12"></polyline>
					</svg>
					<span>¡Copiado!</span>
				`,setTimeout(()=>{t.innerHTML=o},2500)}catch(o){console.error("Error al copiar al portapapeles:",o)}}),i&&i.addEventListener("submit",o=>{o.preventDefault();const n=document.getElementById("contactName"),a=document.getElementById("contactEmail"),r=document.getElementById("contactSubject"),c=document.getElementById("contactMessage"),m=(n==null?void 0:n.value.trim())||"",d=(a==null?void 0:a.value.trim())||"",u=(r==null?void 0:r.value.trim())||"Contacto desde portafolio web",l=(c==null?void 0:c.value.trim())||"";if(!l){e&&(e.className="form-status visible error",e.textContent="Por favor escribe un mensaje antes de enviar.");return}const g=encodeURIComponent(`Hola Guillermo,

${l}

---
De: ${m} (${d})`),v=encodeURIComponent(`[Portafolio] ${u}`),y=`mailto:${s}?subject=${v}&body=${g}`;e&&(e.className="form-status visible success",e.textContent="Abriendo tu cliente de correo para enviar el mensaje... Si no se abre, puedes escribir directamente a druxorey@gmail.com."),window.location.href=y})});
