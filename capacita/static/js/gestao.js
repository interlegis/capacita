$("#gestorInput").on('change', function () {
            console.log($(`option[value="${$(this).val()}"]`).data("id"));
        });