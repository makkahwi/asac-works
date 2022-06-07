# Lesson 37 Reading

## ES6

### ES6 Syntax and Feature Overview

[Source](https://www.taniarascia.com/es6-syntax-and-feature-overview/)

ES6 is basically the most advanced version of JS coding syntax. Follow table compares ES6 to ES5 in many coding parts & features.

| Coding Part / Function | ES5 Approach | ES6 Approach |
| ---------------------- | ------------ | ------------ |
| variable define        | var: to define hoistable, reassignable & redeclarable variable | let: to define reassignable but not redeclarable or hoistable variable |
| ^^^^^^^^^^^^^^^^^^^^^^ | ^^^^^^^^^^^^ | const: to define a non hoistable, non reassignable & non redeclarable variable |
| functions define & return      | fucntion name(args) {return (content)}  | const name = (args) => (content) |
| Template literals      | var str = "text" + name | let str = \`text ${name}\` |
| Multiline strings      | var str = "text1" + "text2" | let str = `text 1 |
| ^^^^^^^^^^^^^^^^^^^^^^ | ^^^^^^^^^^^^^^^^^^^^^^^^^^^ |            text 2' |
| Object key define | var obj = {a: a, b: b} | const obj = {a, b} |
| Object of functions | var obj = {a: function (c,d) {},b: function (e,f) {}} | const obj = {a(c,d) {}, b(e,f) ()} |
| Destructuring Object | var a = obj.a, var b = obj.b, var c = obj.c | let {a,b,c} = obj |
| Array looping | for (var i = 0; i < arr.length; i++) {console.log(arr[i])} | for (let i of arr) {console.log(i)} |
| Default Params | to default value @ args | let func = (a, b = 2) => {return a+b} |
| Spread Syntax | let arr1 = [1, 2, 3], let arr2 = ['a', 'b', 'c'], let arr3 = [...arr1, ...arr2] | let arr1 = [1, 2, 3], let func = (a, b, c) => a + b + c |

---

## React

### React - Hello World

[Source](https://reactjs.org/docs/hello-world.html)

Simplist react app code...

    const root = ReactDOM.createRoot(document.getElementById('root'));
    root.render(<h1>Hello, world!</h1>);

This required a basic understanding of JS coding to go through.

---

### React - JSX

[Source](https://reactjs.org/docs/introducing-jsx.html)

    const element = (
      <div>
        <h1>Hello, world!</h1>
        <h2>This is Suhaib</h2>
      </div>
    );

JSX the the react extention of JS syntax. Which complies the elments rending with the intercation of dynamic parts of the code.

---

### React - Rendering Elements

[Source](https://reactjs.org/docs/rendering-elements.html)

Text

---

### React - Components & Props

[Source](https://reactjs.org/docs/components-and-props.html)

Text

---

### React - State & Lifecycle

[Source](https://reactjs.org/docs/state-and-lifecycle.html)

Text

---

### React - Handling Events

[Source](https://reactjs.org/docs/handling-events.html)

Text

## Tailwind

### Utility First CSS

[Source](https://tailwindcss.com/docs/utility-first)

Text

---

### Tailwind in 15 minutes

[Source](https://www.youtube.com/watch?v=6zIuAyLZPH0)

Text

## Next.js

### Learn Next.js

[Source](https://nextjs.org/learn/basics/create-nextjs-app)

Text

---

### Why to use Next.js

[Source](https://www.youtube.com/watch?v=rtgbaKBhdkk)

Text
