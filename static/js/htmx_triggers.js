/*jshint esversion: 11 */

htmx.on("openModal", (event) => {
    'use strict';
    let modal = new bootstrap.Modal(document.getElementById(`${event.detail.value}`));
    modal.show();
});