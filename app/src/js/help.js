import marked from 'marked'
import '/app/src/css/markdown.css'

let lang = document.documentElement.lang;
let page = document.documentElement.title;

fetch(`/help/${page}_${lang}.md`)
    .then(response => {
        if (response.ok)
            return response.text()
        else return Promise.reject('Not available help');
    })
    .then(value => {
        return document.getElementById('help_content').innerHTML = marked(value);
    })
    .catch(reason => {
        console.log(reason);
        document.getElementById('bs-canvas-right').style.display = "none";
        document.getElementById('nav_help').style.display = "none";
    });

