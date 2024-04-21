let btn = document.querySelector("#send");
let txt = document.querySelector("#user_txt");
const msgs = document.querySelector(".msgs");

btn.addEventListener("click",startChanting);
let thres = false;
function startChanting(value){
    thres = true;
    if(thres == true){
        if(document.getElementById('idx')){
        msgs.removeChild(document.getElementById('idx'))
        }
        thres = false;
    }

    let val = txt.value || value;
    console.log(val)
    form_user_cell(val);
    msgs.scrollTop = msgs.scrollHeight;
    let query = "fetch"

    fetch(query,{
        method:"POST",
        headers:{
            'Content-Type': 'application/json'
        },
        body:JSON.stringify({msg:val})
    }).then(response=>{
        if(response.ok){
            return response.json()
        }
    }).then(data=>{
        console.log(data);
        form_cells(data);
        msgs.scrollTop = msgs.scrollHeight;
    }).catch(err=>{
        console.log(err);

    })
    
}
let j=0
function form_user_cell(val){
    j++;
    const main_res = document.createElement("div");
    let id = `ids_${j}`
    main_res.setAttribute("id",id);
    main_res.setAttribute('class','ask');
    msgs.appendChild(main_res);
    document.getElementById(id).innerHTML = val;
}
let i = 0;
function form_cells(data){
    i++;
    const main_res = document.createElement("div");
    let id = `id_${i}`
    main_res.setAttribute("id",id);
    main_res.setAttribute('class','res');
    msgs.appendChild(main_res);
    document.getElementById(id).innerHTML = data.res;
}
function model(){
    const main_res = document.createElement("div");
    const main_res1 = document.createElement("div");
    const main_res2 = document.createElement("div");
    const main_res3 = document.createElement("div");
    const main_res4 = document.createElement("div");
    let id = `idx`
    main_res.setAttribute("id",id);
    main_res.setAttribute('class','ques');
    msgs.appendChild(main_res);
    main_res1.innerHTML = "Germany";
    main_res2.innerHTML = "Mathematics";
    main_res3.innerHTML = "Linux";
    main_res4.innerHTML = "Atom";

    main_res1.addEventListener('click',send);
    main_res2.addEventListener('click',send);
    main_res3.addEventListener('click',send);
    main_res4.addEventListener('click',send);


    main_res.appendChild(main_res1);
    main_res.appendChild(main_res2);
    main_res.appendChild(main_res3);
    main_res.appendChild(main_res4);
}
model();
function send(){
    thres = true;
 startChanting(this.innerHTML);
}
window.addEventListener('keypress',(e)=>{
    if(e.key == "Enter"){
        startChanting();
    }
})