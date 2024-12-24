// const posts = document.querySelectorAll('.post')

// posts.forEach(element =>{
//     gsap.from(element , {
//         x:100,
//     opacity:0.5,
    
//     scrollTrigger:{

//         tigger:element,
//         scroller :"body",
//         marker:true,
//         scrub:2,



//     },
//     })
// })
const posts = document.querySelectorAll('.post');

posts.forEach(element => {
    gsap.from(element, {
        x: 50,
        opacity: 0.0,
        scrollTrigger: {
            trigger: element, // Corrected to use each element as the trigger
            scroller: "body",
              // Corrected property name
            scrub: 5,
        },
    });
});

// gsap.from(".post" , {
//     x:100,
//     opacity:0.5,
    
//     scrollTrigger:{

//         tigger:".Posts .posts",
//         scroller :"body",
//         marker:true,
//         scrub:2,



//     },
    
// })