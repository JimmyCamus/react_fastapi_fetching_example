import { useEffect, useState } from "react";
const API_URL = "http://localhost:8000";

function App() {
  const [todos, setTodos] = useState([]); // Store the to-do's
  const [formValues, setFormValues] = useState({ title: "", description: "" }); // Store the form inputs values
  useEffect(() => {
    // Obtaining data at page load time
    const getTodos = async () => {
      const res = await fetch(`${API_URL}/todos`); // The request is made to the API to obtain the to-do's, by default the method that fetch has when making a request is GET, so in this case it is not necessary to specify it.
      const todos = await res.json(); // The API response is formatted in json format.
      setTodos(todos); // The data obtained are stored in the to-do's state.
    };
    getTodos();
  }, []);
  const createTodo = async () => {
    // The request is made to the API, to create a what to do you must make a request with the POST method, this must be defined as shown in the line below.
    const res = await fetch(`${API_URL}/todos`, {
      method: "POST",
      body: JSON.stringify({
        title: formValues.title,
        description: formValues.description,
        is_active: true,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    const createdTodo = await res.json(); // The API response is formatted in json format.
    setTodos([...todos, createdTodo]); // The created to do is added to the to-do's state.
    // IMPORTANT. To perform other request such as updating or deleting, you can do it in the same way, just change the method to the corresponding one.
  };
  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        flexDirection: "column",
      }}
    >
      <h1>FETCHING DATA EXAMPLE</h1>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          flexDirection: "column",
        }}
      >
        <h2>Create Todo</h2>
        <section>
          <input
            placeholder="title"
            value={formValues.title}
            onChange={(e) =>
              setFormValues({ ...formValues, title: e.target.value })
            }
          />
          <input
            placeholder="description"
            value={formValues.description}
            onChange={(e) =>
              setFormValues({ ...formValues, description: e.target.value })
            }
          />
          <button onClick={createTodo}>Create</button>
        </section>
        <h2>Todos</h2>
        <section style={{ width: "50%" }}>
          <table
            style={{
              width: "100%",
              tableLayout: "fixed",
              border: "1px solid ",
            }}
          >
            <thead>
              <tr>
                <th>Title</th>
                <th>Description</th>
                <th>Is active</th>
              </tr>
            </thead>
            <tbody>
              {todos.map((todo) => (
                <tr key={todo.id}>
                  <td style={{ padding: "12px" }}>{todo.title}</td>
                  <td>{todo.description}</td>
                  <td>{todo.is_active ? "True" : "False"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      </div>
    </div>
  );
}

export default App;
