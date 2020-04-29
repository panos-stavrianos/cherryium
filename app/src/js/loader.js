import '/app/src/css/loader.css'

export function loader_show() {
    $("div.spanner").addClass("loader_show");
    $("div.overlay").addClass("loader_show");
}

export function loader_hide() {
    $("div.spanner").removeClass("loader_show");
    $("div.overlay").removeClass("loader_show");
}