# Lesson 38 Reading

## React - Conditional Rendering

[Source](https://reactjs.org/docs/conditional-rendering.html)

It's basically about how to apply the conditional rendering for a component, where the component is to be rendered if the condition applies. So in case a specific data object need to be reflected in a specific view like a table, if condition could be applied to check if data exists so the view would be rendered.

        {data && (
            <table>
                <tr>
                    <th>
                        {data.key}
                    </th>
                    <td>
                        {data.value}
                    </td>
                </tr>
            </table>
        )}

---

## React - Lists & Keys

[Source](https://reactjs.org/docs/lists-and-keys.html)

This is about using dynamic lists renderednig in the views. So if a list of objects are to be rendered, .map() function could be used so a loop would go through the list and rendered it using the same source code.

        const employees = [{
            name: "Suhaib"
            position: "React Developer"
        }, {
            name: "Hadi"
            position: "Django Developer"
        }];

        <table>
            <theader>
                <tr>
                    <th>
                        Name
                    </th>
                    <th>
                        Position
                    </th>
                </tr>
            </theader>
            <tbody>
                {employees.map(employee => (
                    <tr>
                        <th>
                            {employee.name}
                        </th>
                        <td>
                            {employee.position}
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>

---

## React - Forms

[Source](https://reactjs.org/docs/forms.html)

Form tags in react are the exact same ones of HTML, but they could have some more properties to define their function & ease their build work.

        <form>
            <input name="title" type="text" required />

            <select name="job">
                <option value="FE dev">
                    Frontend Developer
                </option>

                <option value="BE dev">
                    Backend Developer
                </option>
            </select>

            <select name="department" value=["IT", "Finance", "HR"]/>

            <input name="profilePhoto" type="file" />
        </form>

---

## React - Lifting State

[Source](https://reactjs.org/docs/lifting-state-up.html)

Text

---

## React - Composition vs Inheritance

[Source](https://reactjs.org/docs/composition-vs-inheritance.html)

Text

---

## Thinking in React

[Source](https://reactjs.org/docs/thinking-in-react.html)

Text
