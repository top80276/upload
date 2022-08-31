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


// 首頁連接
app.get('/',(req,res)=>{
    res.render('index');
 });




// 人臉分析
 app.get('/analyze',function(req,res) {
    res.render('./analyze/analyze',{});
});

app.post('/analyze1', upload.single('photo'),  function(req, res){
    // console.log(req.file); // 查看裡面的屬性
    if (req.file && req.file.originalname) {
        // 判斷是否為圖檔
        if (/\.(jpg|jpeg|png|gif)$/i.test(req.file.originalname)) {
            // 將檔案搬至公開的資料夾
            fs.rename(req.file.path, './public/img/001.jpg' , error => { });

            // 執行Face_Analyze.py程式並傳回值
            PythonShell.run('Face_Analyze.py', null,  function(err, data) {
            if (err) throw err;
            // var results = await JSON.stringify(data)
            var results = data.slice(-5,-1)
            // var results = data
            console.log(results);
            res.render('./analyze/analyze_python',{results});   
    
          });
    }
         }  else {
            fs.unlink(req.file.path, error => { }); // 刪除暫存檔                     
    }     
});





// 人臉比對
app.get('/ver',function(req,res) {
    res.render('./ver/ver',{});
});

var files = [{ name: 'photo1' }, { name: 'photo2' }]
app.post('/ver1', upload.fields(files), async function (req, res) { //async 

    //存照片
    for (let i = 0; i < files.length; i++) {
      if (/\.(jpg|jpeg|png|gif)$/i.test(req.files[files[i].name][0].originalname)) {
        fs.createReadStream(req.files[files[i].name][0].path).pipe(
          fs.createWriteStream('./public/img/ver' + [i] + '.jpg')
        )
      };
    }
    PythonShell.run('Face_Verification.py', null, async function (err, data) {
      // 將update的照片檔名弄成object
        Obj={fileName:req.files[files[0].name][0].originalname}
        Obj1={fileName1:req.files[files[1].name][0].originalname}
        var results = await JSON.stringify(data)
        var results = data.slice(-5, -1) 
        console.log(results);
        res.render('./ver/ver_python', { results });
    });
  });





// 群眾分析
  app.get('/mtcnn',function(req,res) {
    res.render('./mtcnn/mtcnn',{});
});

app.post('/mtcnn1', upload.single('photo'),  function(req, res){
  // console.log(req.file); // 查看裡面的屬性
  if (req.file && req.file.originalname) {
      // 判斷是否為圖檔
      if (/\.(jpg|jpeg|png|gif)$/i.test(req.file.originalname)) {
          // 將檔案搬至公開的資料夾
          fs.rename(req.file.path, './public/img/mtcnn1.jpg' , error => { });

          // 執行Face_Analyze.py程式並傳回值
          PythonShell.run('MTCNN.py', null,  function(err, data) {
          if (err) throw err;
          // var results = await JSON.stringify(data)
          var results = data.slice(-5,-1)
          // var results = data
          console.log(results);
          res.render('./mtcnn/mtcnn_python',{results});   
  
        });
  }
       }  else {
          fs.unlink(req.file.path, error => { }); // 刪除暫存檔                     
  }     
});




// Webcam
app.get('/cam',function(req,res) {
  res.render('./cam/cam',{});
});


app.get('/cam1',function(req,res) {
  PythonShell.run('Webcamhaar.py', null,  function(err, data) {
    if (err) throw err;
    // var results = await JSON.stringify(data)
    var results = data.slice(5,6)
    console.log(results);

  res.render('./cam/cam_python',{results});
});
});