function editnote(buttonid) {
    var fired_button = $(buttonid).val();
    alert(fired_button);
    document.getElementById("inputbar").value = document.getElementById(fired_button).innerText;
};