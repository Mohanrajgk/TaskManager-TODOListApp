import TodoItem from './Todo'

function TodoView(Props){
    return (
        <div>
            <ul>
                {props.todoList.map(todo => <TodoItem todo= {todo}/>)}
            </ul>
        </div>
    )
}
export default TodoView