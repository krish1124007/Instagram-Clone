const throtitle = document.querySelectorAll('.throtitle');
const thropara = document.querySelectorAll('.thropara');


const Titleup = () =>{
const inputTitleValue = document.getElementById('titleValue').value;

    throtitle.forEach(element =>{
        element.innerHTML = inputTitleValue;
    })
}

const Paraup = () => {
const inputParaValue = document.getElementById('paraValue').value;

    thropara.forEach(element=>{
        element.innerHTML = inputParaValue;
    })
}