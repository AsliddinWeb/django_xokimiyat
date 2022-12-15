const check = document.querySelector('#check');
const noCheck = document.querySelector('#no-check');

const selectOpt = document.querySelector('#exampleNogironligi');

selectOpt.style.display = "none";


check.addEventListener('change' , function(){
    if (this.checked) {
        selectOpt.style.display = "block";
    }
})

noCheck.addEventListener('change' , function(){
    if (this.checked) {
        selectOpt.style.display = "none";
    }
})

