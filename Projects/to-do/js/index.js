function getToDoDB(){
    // return DB from localStorage
    var base_data = {
        "to_do" : [
            getTask(message="Sample task", is_done=false)
        ]
    };
    if( !localStorage.getItem("to-do") ){
        localStorage.setItem("to-do", JSON.stringify(base_data));
    }

    return JSON.parse(localStorage.getItem("to-do"));
}

function getChecked(task){
    // if a task was done or not
    return (task.is_done ? "checked" : "");
}

function getTask(message="", is_done=false){
    // craft a Task object
    return {
        "message" : message,
        "is_done" : is_done,
        "date": Date.now()
    }
}
    

function formatTask(task){
    // return HTML formated task
    return '<li class="task">'+
              '<span class="task_message">'+
                task.message +
               '</span>'+

              '<input class="task_check" type="checkbox"'+ 
                getChecked(task) + 
              ' ></input>'+
           '</li>' 
}

function populate(){
    // populate the view with data from localStorage
    var data = getToDoDB();
    console.log(data.to_do)
    $("#list").empty()
    for(var i = data.to_do.length-1; i>=0; i--){
        $("#list").append(formatTask(data.to_do[i]));
    }
}

$( document ).ready(function() {
    populate();


    $("#add").click(function(){
        var task_name = $("#input").val(),
            data = getToDoDB(),
            new_task = getTask(message=task_name);

        data.to_do.push(new_task);
        localStorage.setItem("to-do", JSON.stringify(data))

        populate();
    })
});


