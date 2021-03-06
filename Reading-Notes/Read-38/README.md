# Lesson 38 Reading

Navigation | [Past Reading](../Read-37/README.md) | [Home Page](../README.md) | Next Reading |

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

As react components are built in a tree form, if there are common states & variables to be used in more than one separate component, this state / variable need to be place in the closest common parent component, and passed through the props of the child components.

                                homepage
                              /           \
                  features                    services
                /         \                  /        \
            feature 1   feature 2       service 1   service 2

So assuming in the example above that a state need to be used in both components of "service 1" & "service 2", the state need to be initiated inside the common "services" component, and passed through props of both children. So inside parent component of "services", state to be initiated and passed as follows.

        const [state, setState] = useState("")

        <Service1 state={state} setState={setState} />
        <Service2 state={state} setState={setState} />

And inside each child component, the state and it's setter are to be recieved in the props as follows.

        const Service1 = props => {
            const {state, setState} = props
            .
            .
            .
        };

        const Service2 = ({state, setState}) => {
            .
            .
            .
        };

So when a state is initiated, there should be consideration about the components to use the state, so the hosting component of the state could be decided righty.

---

## React - Composition vs Inheritance

[Source](https://reactjs.org/docs/composition-vs-inheritance.html)

In above example, it was shown how anything (data, state, function or even component) could be passed from a parent component to a child using the props approach. In that example, the passed values were defined with specific titles / keys, and using those keys in the child, the passed arguments are received and processed or showed.

Another way to pass arguments to children components is using child prop. This is useful in case of wanting to avoid using specific keys, which properly is needed in case of having unknown / various arguments to pass to child component. It's to be passed as follows...

        <Service1>
            # Elements to pass
            <h2>This is the begining of</h2>
            <h3>World War III</h3>
        </Service1>

and recieved as follows...

        const Service1 = props => {
            const {children} = props
            return (
                <div>
                    <h1>Hello</h1>
                    # Passed Elements
                    {children}
                </div>
            )
        };

this is gonna be exactly like coding it this way...

        const Service1 = () => {
            return (
                <div>
                    <h1>Hello</h1>
                    <h2>This is the begining of</h2>
                    <h3>World War III</h3>
                </div>
            )
        };

---

## Thinking in React

[Source](https://reactjs.org/docs/thinking-in-react.html)

As a frontend developer, you're supposed to get the UI/UX designs to code. So if a UI of a page is received, React.js developer should...

- start breaking the UI into separate components & a hierarchy of them
- Then the static version of UI is to be coded with consideration of proposed / planned structure ot components.
- Identify the uses of states & dynamic data within coded components.
- Decide & place each state in the hosting component.
- Build the dynamic controls of place states.
