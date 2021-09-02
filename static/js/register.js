$(function () {
    $("#id_fecha_nacimiento").datepicker({
        format: 'dd/mm/yyyy',
        // If true or “linked”, displays a “Today” button at the bottom of the datepicker to select the current date.
        // If true, the “Today” button will only move the current date into view; if “linked”, the current date will also be selected.
        todayBtn: true,
        // The latest date that may be selected; all later dates will be disabled
        endDate: '+0d',
    });
});