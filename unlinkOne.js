const express = require('express');
const app = express();
let { PythonShell } = require('python-shell')
app.listen(8181);

const multer = require('multer');
const upload = multer({ dest: "uploads" }); // 設定上傳暫存目錄
const fs = require('fs'); // 處理檔案的核心套件

app.use(express.static('public'));
app.set('view engine','ejs');







app.post('/', upload.single('photo'), (req, res) => {
    // console.log(req.file); // 查看裡面的屬性
    if (req.file && req.file.originalname) {
        // 判斷是否為圖檔
        if (/\.(jpg|jpeg|png|gif)$/i.test(req.file.originalname)) {
            // 將檔案搬至公開的資料夾
            fs.rename(req.file.path, './public/img/001.jpg' , error => { });

   
        PythonShell.run('Face_Analyze.py', null, function (err, data) {
            if (err) throw err;
            const results = JSON.parse(data)
            // console.log(results);
          });
    }
         }  else {
            fs.unlink(req.file.path, error => { }); // 刪除暫存檔
        
            
    }
    // res.end('image uploaded successful');

    res.render('uploadOne',{results});

});

app.get('/',function(req,res) {
    res.render('uploadOne',{});
});

