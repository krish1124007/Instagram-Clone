const data = document.querySelectorAll('.mli')
const classdata = document.querySelectorAll('.chat-shower')

const localdataget = localStorage.getItem('displayid')
console.log("this is a localdataget",localdataget);

classdata.forEach((element) =>{
    if(element.id==localdataget)
    {
        element.style.display = 'flex'
    }
    else{
        element.style.display ='none'
    }
})

data.forEach((element) => {
    element.addEventListener('click', () => {
        classdata.forEach(classelement => {
            
            if (element.id == classelement.id) {
                
                const localdata = localStorage.setItem('displayid' , element.id)
                classelement.style.display = "flex"

            }
            else {

                classelement.style.display = "none"
            }


        });
    })
})



