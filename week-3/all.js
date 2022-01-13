let data = []
let num1 = 0;
let num2 = 8;
getData();

// 取得 JSON 資料
function getData(){
    const dataUrl = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
    let xhr = new XMLHttpRequest();
    xhr.open('GET', dataUrl, true);
    xhr.send();
    xhr.onload = function(){
        let datas = JSON.parse(this.responseText);
        data = datas.result.results;
        renderPicture(0,8)
    }
}

function renderPicture(num1, num2){
    const pictureSection = document.querySelector('.content');
    // 建立一個 DocumentFragment，可以把它看作一個「虛擬的容器」
    let fragment = document.createDocumentFragment();

    for(let i=num1; i<num2; i++){
        // 取得第一張照片的網址
        picIndex = data[i].file.toLowerCase().indexOf('jpg');
        picUrl = data[i].file.substring(0,picIndex+3);

        // 組成標籤放入 html 中
        let li = document.createElement("li");

        // 圖片
        let pic = li.appendChild(document.createElement("div"));
        pic.setAttribute("class","adjustPic");
        pic.style['background-image'] = `url(${picUrl})`;

        // 風景名稱
        let picDescription = li.appendChild(document.createElement("p"));
        title = document.createTextNode(data[i].stitle);
        picDescription.appendChild(title);

        // 放入虛擬容器
        fragment.appendChild(li);
    }
    
    pictureSection.appendChild(fragment);
}

const loadBtn = document.querySelector('.loadBtn');
loadBtn.addEventListener('click',function(e){
    num1 +=8;
    num2 +=8;

    // 如果 num1 大於資料陣列的長度就不執行
    if(num1 < data.length){
        // 如果 num2 大於陣列長度，其值等於陣列長度的值
        if(num2 > data.length){
            num2 = data.length;
        }
        // console.log(num1,num2)
        renderPicture(num1, num2)
    }
})
    