(this.webpackJsonphackathonfront=this.webpackJsonphackathonfront||[]).push([[0],{104:function(e,t,a){"use strict";a.r(t);var c=a(0),n=a(17),s=a.n(n),i=(a(69),a.p+"static/media/logo.3ff59aa8.svg"),r=(a.p,a(111)),o=a(106),j=a(64),l=a(109),b=a(1),d=function(){return Object(b.jsx)(r.a,{expand:!1,children:Object(b.jsxs)(o.a,{fluid:!0,children:[Object(b.jsx)(r.a.Brand,{href:"/",children:Object(b.jsx)("img",{src:i,width:"100",height:"50",className:"d-inline-block align-top",alt:"React Bootstrap logo"})}),Object(b.jsx)(r.a.Toggle,{"aria-controls":"offcanvasNavbar"}),Object(b.jsxs)(r.a.Offcanvas,{id:"offcanvasNavbar","aria-labelledby":"offcanvasNavbarLabel",placement:"end",children:[Object(b.jsx)(j.a.Header,{closeButton:!0,children:Object(b.jsx)(j.a.Title,{id:"offcanvasNavbarLabel",children:"MENU"})}),Object(b.jsx)(j.a.Body,{children:Object(b.jsxs)(l.a,{className:"justify-content-end flex-grow-1 pe-3",children:[Object(b.jsx)(l.a.Link,{href:"/inbox",children:"Inbox"}),Object(b.jsx)(l.a.Link,{href:"/today",children:"Today"}),Object(b.jsx)(l.a.Link,{href:"/upcoming",children:"Upcoming"})]})})]})]})})},O=a(8),h=a(107),m=a(108),x=a(40),u=a.n(x),f=a(6),p=a(2),g=a(110),v=a(61),y=a(56),k=a.n(y),N=(a(94),a(44)),D=a.n(N),T=a(57),C=a.n(T),P=a(58),S=a.n(P),_=a(59),w=a.n(_),L=a(60),I=a.n(L),B=(a(102),function(e){var t=Object(c.useState)([]),a=Object(O.a)(t,2),n=a[0],s=a[1],i=Object(c.useState)([]),r=Object(O.a)(i,2),o=(r[0],r[1]);return Object(b.jsx)(D.a,Object(f.a)({range:!0,calendarPosition:"bottom-center",fixMainPosition:!0,format:"MM/DD/YYYY HH:mm",value:n,animations:[C()()],onChange:function(e){s(e),o(Object(N.getAllDatesInRange)(e))},plugins:[Object(b.jsx)(S.a,{position:"bottom",hideSeconds:!0,style:{minWidth:"100px"}}),Object(b.jsx)(I.a,{markFocused:!0})],render:Object(b.jsx)(w.a,{})},"onChange",e.handler))}),E=Object.freeze({userTask:"",userDesc:"",userPriority:"",startDate:"",startTime:"",endDate:"",endTime:""}),z=function(e){var t=Object(c.useState)(""),a=Object(O.a)(t,2),n=a[0],s=a[1],i=Object(c.useState)(E),r=Object(O.a)(i,2),j=r[0],l=r[1],d=function(e){if(e.value||e.length)if(e.length){var t,a;if(2==e.length)l(Object(p.a)(Object(p.a)({},j),{},(t={},Object(f.a)(t,"startDate","".concat(e[0].month.number,"/").concat(e[0].day,"/").concat(e[0].year)),Object(f.a)(t,"startTime","".concat(e[0].hour,":").concat(e[0].minute)),Object(f.a)(t,"endDate","".concat(e[1].month.number,"/").concat(e[1].day,"/").concat(e[1].year)),Object(f.a)(t,"endTime","".concat(e[1].hour,":").concat(e[1].minute)),t)));else l(Object(p.a)(Object(p.a)({},j),{},(a={},Object(f.a)(a,"startDate","".concat(e[0].month.number,"/").concat(e[0].day,"/").concat(e[0].year)),Object(f.a)(a,"startTime","".concat(e[0].hour,":").concat(e[0].minute)),a)))}else l(Object(p.a)(Object(p.a)({},j),{},Object(f.a)({},"userPriority",e.value)));else s(e.target.value),l(Object(p.a)(Object(p.a)({},j),{},Object(f.a)({},e.target.name,e.target.value.trim())))},x=["No priority","Priority 1","Priority 2","Priority 3","Priority 4"];return Object(b.jsxs)(o.a,{className:"mb-5",children:[Object(b.jsx)(g.a,{children:Object(b.jsxs)(g.a.Group,{className:"mb-3",controlId:"exampleForm.ControlInput1",children:[Object(b.jsx)(g.a.Control,{type:"text",placeholder:"Task's name",name:"userTask",onChange:d}),Object(b.jsx)(g.a.Control,{as:"textarea",rows:3,placeholder:"Task's description",name:"userDesc",onChange:d}),Object(b.jsxs)(h.a,{children:[Object(b.jsx)(v.a,{className:"mt-2",sm:12,lg:6,children:Object(b.jsx)(k.a,{options:x,value:x[0],placeholder:"Select an option",name:"userPriority",onChange:d})}),Object(b.jsx)(v.a,{className:"mt-3",sm:12,lg:6,children:Object(b.jsx)(B,{handler:d})})]})]})}),Object(b.jsxs)(h.a,{className:"mt-2",children:[Object(b.jsx)(v.a,{xs:6,sm:2,lg:1,children:Object(b.jsx)(m.a,{variant:"dark",disabled:!n,size:"sm",onClick:function(t){t.preventDefault(),console.log(j),u()({method:"POST",url:"http://127.0.0.1:8000/api/to_do_list/",task:E.userTask,description:E.userDesc,start_data:E.startDate,end_data:E.endDate,start_time:E.startTime,end_time:E.endTime,priority:E.userPriority}).then((function(e){console.log(e)})).catch()((function(e){console.log(e)})),e.func()},children:"ADD"})}),Object(b.jsx)(v.a,{xs:6,sm:2,lg:1,children:Object(b.jsx)(m.a,{variant:"dark",size:"sm",onClick:function(){e.func()},children:"CANCEL"})})]})]})},A=function(e){return Object(b.jsxs)("div",{className:"task",children:[Object(b.jsx)(h.a,{children:Object(b.jsx)("h4",{children:e.name})}),Object(b.jsx)(h.a,{children:Object(b.jsx)("i",{children:e.desc})}),Object(b.jsx)(h.a,{})]})},M=function(e){var t=Object(c.useState)(!1),a=Object(O.a)(t,2),n=a[0],s=a[1],i=Object(c.useState)([]),r=Object(O.a)(i,2),j=r[0],l=r[1];function d(){s(!n)}Object(c.useEffect)((function(){u()({method:"GET",url:"http://127.0.0.1:8000/api/to_do_list/"}).then((function(e){l(e.data),console.log(e)}))}),[]);var x=new Date;return Object(b.jsxs)(o.a,{children:["today"===e.action&&Object(b.jsxs)("div",{children:[Object(b.jsx)("h2",{children:"Today"}),Object(b.jsx)("i",{children:x.toDateString()})]}),"inbox"===e.action&&Object(b.jsxs)("div",{children:[Object(b.jsx)("h2",{children:"Inbox"}),Object(b.jsx)(h.a,{className:"taskList",children:j.map((function(e){return Object(b.jsx)(A,{name:e.task,desc:e.description},e.id)}))})]}),n&&Object(b.jsx)("div",{children:Object(b.jsx)(h.a,{className:"mt-2",children:Object(b.jsx)(z,{func:d})})}),!n&&Object(b.jsx)(h.a,{className:"m-4",children:Object(b.jsx)(m.a,{variant:"warning",size:"sm",onClick:function(){d()},children:"Add task"})})]})},Y=a(62),H=a(7);var F=function(){return Object(b.jsxs)("div",{className:"page",children:[Object(b.jsx)(d,{}),Object(b.jsx)(o.a,{className:"main",children:Object(b.jsx)(h.a,{className:"justify-content-md-center mt-2",children:Object(b.jsx)(Y.a,{children:Object(b.jsxs)(H.c,{children:[Object(b.jsx)(H.a,{path:"/",element:Object(b.jsx)(M,{action:"today"})}),Object(b.jsx)(H.a,{path:"/today",element:Object(b.jsx)(M,{action:"today"})}),Object(b.jsx)(H.a,{path:"/inbox",element:Object(b.jsx)(M,{action:"inbox"})})]})})})})]})};a(103);s.a.render(Object(b.jsx)(F,{}),document.getElementById("root"))},69:function(e,t,a){}},[[104,1,2]]]);
//# sourceMappingURL=main.e6c92b1b.chunk.js.map