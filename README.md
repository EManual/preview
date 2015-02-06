preview
=======

markdown preview for EManual


usage-构建新`preivew.html`
-----

#### step 1 修改资源映射文件`map.json`

example:  
```json
[
  { 
    "type":"script",
    "file":"./static/js/highlight.pack.js"
  },
    ..............
  { 
    "type":"link",
    "file":"./static/css/github-markdown.css"
  }
]
```  

#### step 2
```shell
./build.py
```

构建后的`preview.html`在`dist/`下


License
------- 

   Copyright 2015 EManual

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
