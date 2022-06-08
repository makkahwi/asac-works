# Lesson 37 Reading

Navigation

| [Past Reading](../Read-36/README.md) | [Home Page](../README.md) | [Next Reading](../Read-38/README.md) |
| ------------ | --------- | ------------ |

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

The main feature of React is the ability to rerender only what needs a re render instead of re rendering a whole page / app. In below example it's to be seen that only element which contains date/time is what would be rerendered on date/time update.

    const root = ReactDOM.createRoot(
      document.getElementById('root')
    );

    function tick() {
      const element = (
        <div>
          <h1>Hello, world!</h1>
          <h2>It is {new Date().toLocaleTimeString()}.</h2>
        </div>
      );
      root.render(element);
    }

    setInterval(tick, 1000);
---

### React - Components & Props

[Source](https://reactjs.org/docs/components-and-props.html)

The above element-oriented render has been reproduced in react using the component concept. Which is about splitting an app into page components, and each page into smaller components according to their functionality & rerender needs. Those split components are to be linked in a tree-like structure, where a component might have one parent but several children. And so variable and data could be passed between the components according to the tree structure.

                                homepage
                              /           \
                  features                    services
                /         \                  /        \
            feature 1   feature 2       service 1   service 2

So each of those parts could be a separate component in react coding. And in case of having to pass data from "service 1" component to "feature 1" component, this data is to be stored in "homepage" component and it's updating function is to be passed through the parent components of "features" & "services" to "feature 1" & "service 1". In this structure, in case of updating some data stored in "service 1" component, only this component is to be rerendered instead of rerendering "homepage" and all of its children.

---

### React - State & Lifecycle

[Source](https://reactjs.org/docs/state-and-lifecycle.html)

In case of having JS clases, it's possible to have local states (variables) to pass data between different locations or to make it dynamic data. This state is recommended to have own already-built function to update it instead of using reassigning approach. In react hooks, there is a useState hook which to do the both of having dynamic states & updating them.

---

### React - Handling Events

[Source](https://reactjs.org/docs/handling-events.html)

Many HTML & react built-in items / components have what are called as events. Most common events are onChange and onClick and onSubmit events. This allows to build a whole function to do several steps in case of the occurrence of the event linked to the function.

    const onInputChange = value => console.log(value)

    const func = () => {
      <input type="text" onChange={e => onInputChange(e.target.value)} />
    }

## Tailwind

### Utility First CSS

[Source](https://tailwindcss.com/docs/utility-first)

Tailwind is basically a styling library to be used with React. Like Bootstrap, it's a set of pre-built styling classes which are to be applied to appropriate items / elements / components in React. The so-many options offered by such libraries, it saves the time of building own styling classes or doing inline styling. With time and extensive usage, 70 - 80% of those pre-built classes would be remembered and smoothly called upon need.

---

### Tailwind in 15 minutes

[Source](https://www.youtube.com/watch?v=6zIuAyLZPH0)

Given video is unavailable. Returns "Video unavailable This video is private" msg.

## Next.js

[Source](https://nextjs.org/learn/basics/create-nextjs-app)
[Source](https://www.youtube.com/watch?v=rtgbaKBhdkk)

As React.Js is actually a library not a framework, Next.js is the react-based framework which handles many of the react issues of loose ends & over flexibility such as...

- Involvement a bundler like webpack and a compiler like Babel.
- Production optimizations like code splitting.
- To pre-render some pages for performance and SEO & some server-side rendering or client-side rendering.
- To connect React app to  data store.

Next.js offeres following features / uses...

- To build scalable react apps with some react complexity.
- To pick whether to render on client side or server side or mix of both.
- Pick data fetching strategy.
- Hooks to generate static website from dynamic data for users like SEO.
- Do the split coding work for performance uses.
- Webpack enhancement.
- Debugging assistant.
