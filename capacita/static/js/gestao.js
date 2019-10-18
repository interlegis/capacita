$("#gestorInput").on('change', function () {
    let user = $(`option[value="${$(this).val()}"]`).data("id");
    if (user == null) {
        $("#addGestor").addClass('disabled');
    } else {
        $("#addGestor").removeClass('disabled');
        $("#novoGestor").val(user);
    }
});