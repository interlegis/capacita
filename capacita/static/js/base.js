$('.ui.dropdown').dropdown();
$('.ui.accordion').accordion();
$('.ui.checkbox.permitido').checkbox('set checked');
$('.ui.checkbox.sem_permissao').checkbox('set unchecked');

 $('input.sem_permissao').on('change', function(){
    $.ajax({
    type: "POST",
    url: "/usuarios/permissao/",
    data: {data : 'True', usuario_id : this.value},
    success : function(data) {
      location.reload();
    }
  });
})

$('input.permitido').on('change', function(){
    $.ajax({
    type: "POST",
    url: "/usuarios/permissao/",
    data: {data : 'False', usuario_id : this.value},
    success : function(data) {
      location.reload();
    }
  });
})

function selectTreinamento(){
    $("#id_treinamento").val('')
    $("#id_treinamento option").each(function(){
        $(this).hide();
    });

    var search = $("#id_treinamento").val();
    select = $("#areas").options;

    var areas;
    $.getJSON("/api/treinamentos/", function(data){
        var treinamento = null;
        areas = data;
        if ($("#id_cod_area_conhecimento").val() == ''){
          $("#id_treinamento option").each(function(){
            $(this).show();
          });
        }

        else {
          for(var i = 0; i < data.length; i++){
            if(data[i].cod_area_conhecimento_id == $("#id_cod_area_conhecimento").val() ){
              treinamento = data[i].cod_treinamento;
              $('#id_treinamento option[value="' + treinamento + '"]').show();
            }
          }
          $('#id_treinamento option[value="-1"]').show();
        }
    });
}

function selectSugestao(select){
  treinamento = $("#id_treinamento").val()
  if($('#id_treinamento').val() == -1){
    $('#sugestao').css({'display': 'block'})
    $('#erro_sugestao').css({'display': 'block'})
  }
  else{
    $('#sugestao').css({'display': 'none'})
    $('#erro_sugestao').css({'display': 'none'})
  }

    console.log($("#id_cod_area_conhecimento").val());
  $.getJSON("/api/treinamentos/", function(data){
    for(var i = 0; i < data.length; i++){
      if(data[i].cod_treinamento == treinamento ){
        if (data[i].cod_area_conhecimento != $("#id_cod_area_conhecimento").val())
          if ($("#id_treinamento").val() != -1) {
            console.log(data[i].cod_area_conhecimento_id);
            $("#id_cod_area_conhecimento").val(data[i].cod_area_conhecimento_id)
          }
          break
      }
    }
  });
}

function selectTreinamentoExterno(select){
  treinamento = $("#id_treinamento_externo")[0].checked
  if(treinamento == false){
    $('#erro_valor_estimado').css({'display': 'none'})
    $('#valor_estimado').css({'display': 'none'})
  }
  else{
    $('#erro_valor_estimado').css({'display': 'block'})
    $('#valor_estimado').css({'display': 'block'})
  }

    console.log($("#id_cod_area_conhecimento").val());
  $.getJSON("/api/treinamentos/", function(data){
    for(var i = 0; i < data.length; i++){
      if(data[i].cod_treinamento == treinamento ){
        if (data[i].cod_area_conhecimento != $("#id_cod_area_conhecimento").val())
          if ($("#id_treinamento_externo").val() != -1) {
            $("#id_cod_area_conhecimento").val(data[i].cod_area_conhecimento_id)
          }
          break
      }
    }
  });
}


var tipo;

var planos_externos = [];
var plano;

$.getJSON("/api/planos/", function(data){

    for(var i = 0; i < data.length; i++){
        if(data[i].cod_tipo_plano_capacitacao_id == $("#planos").val()){
            plano = data[i];
        }
        if(data[i].cod_tipo_plano_capacitacao_id == tipo){
            planos_externos.push(data[i].cod_plano_capacitacao);
        }
    }

    console.log(planos_externos);

});

$(document).ready(function(){
    selectSugestao();
    if(tipo == (parseInt($("#id_cod_tipo").val()))){
        $("#id_custoo").prop('disabled', false);
    }else{
        $("#id_custoo").prop('disabled', true);
    }

    $("#descricao_necessidade").prop('disabled', false);


    $("#myInput").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#treinamentos tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});

$("#nome_curso_form").on('change', function(){
    if($("#nome_curso_form option:selected").val() == ''){
        $("#descricao_necessidade").prop('disabled', false);
    }else{
        $("#descricao_necessidade").prop('disabled', true);
    }
})

$("#id_cod_tipo").on('change', function(){
    if(tipo == (parseInt($("#id_cod_tipo").val()))){
        $("#id_custoo").prop('disabled', false);
    }else{
        $("#id_custoo").prop('disabled', true);
    }
})
