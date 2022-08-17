const express = require('express');
const app = express();
let { PythonShell } = require('python-shell')
// Establishing the port
const PORT = process.env.PORT || 3000;
 
// Executing the server on given port number
app.listen(PORT, console.log(
  `Server started on port ${PORT}`));


const multer = require('multer');
const upload = multer({ dest: "uploads" }); // 設定上傳暫存目錄
const fs = require('fs'); // 處理檔案的核心套件

app.use(express.static('public'));
app.set('view engine','ejs');



function sleep(delay) {
    var start = (new Date()).getTime();
    while ((new Date()).getTime() - start < delay) {
        // 使用  continue 实现；
        continue; 
    }
}



app.post('/', upload.single('photo'), async function(req, res){
    // console.log(req.file); // 查看裡面的屬性
    if (req.file && req.file.originalname) {
        // 判斷是否為圖檔
        if (/\.(jpg|jpeg|png|gif)$/i.test(req.file.originalname)) {
            // 將檔案搬至公開的資料夾
            fs.rename(req.file.path, './public/img/' + req.file.originalname , error => { });
            // 執行Face_Analyze.py程式並傳回值
            PythonShell.run('Face_Analyze.py', null, async function(err, data) {
            if (err) throw err;
            // 將update的照片檔名弄成object
            var fileNameObj = {fileName:req.file.originalname}
            var results = await JSON.stringify(data)
            var results = data.slice(-5,-1)
            // 輸出的result是object，將results，fileNameObj合併成一個object
            var result = Object.assign(results, fileNameObj)
            console.log(results);
            // console.log(results);
            res.render('uploadOne_python',{results});   
          });
    }
         }  else {
            fs.unlink(req.file.path, error => { }); // 刪除暫存檔      
    } 
});

// input是uploadOne.ejs
// output是uploadOne_python.ejs
app.get('/',function(req,res) {
    res.render('uploadOne',{});
});


// input是uploadOne_python.ejs
// output是uploadOne_python.ejs
app.get('/',function(req,res) {
    res.render('uploadOne_python',{});
});
