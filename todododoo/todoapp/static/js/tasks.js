let last_tasks = document.querySelector('.last-tasks');
let future_tasks = document.querySelector('.future-tasks');

function showLast() {
    future_tasks.classList.add('none-display');
    future_tasks.classList.remove('block-display');
    last_tasks.classList.add('block-display');
    last_tasks.classList.remove('none-display');
}

function showFuture() {
    future_tasks.classList.remove('none-display');
    future_tasks.classList.add('block-display');
    last_tasks.classList.remove('block-display');
    last_tasks.classList.add('none-display');
}