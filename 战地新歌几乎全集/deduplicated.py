import os
import sys
import json
import uuid
from pathlib import Path
import re
import shutil


all_names = [re.sub(r'^[a-zA-Z0-9_]+', '', item.name) for item in Path('../').iterdir() if item.is_file()]

for i in range(1,6):
    # 获取当前目录的 Path 对象
    current_directory = Path('./' + str(i)) 

    # 使用列表推导式获取当前目录下的所有文件名（不包含子目录中的文件）
    # iterdir() 遍历目录下的所有条目 (文件和文件夹)
    # is_file() 筛选出文件
    file_names = [item.name for item in current_directory.iterdir() if item.is_file()]

    # 打印文件名列表
    for f in file_names:
        fname = os.path.basename(f)
        if fname in all_names:
            print(fname, 'ignored')
        else:
            print(fname)
            id = str(uuid.uuid4())
            meta = {
  "resource_type": 'music',
  "entity": {
    "id": id,
    "name": Path(fname).stem,
    "description": '',
    "lyrics": [
      {
        "content": '',
        "version": '原版',
        "audios": [
          {
            "url": 'https://raw.githubusercontent.com/banned-historical-archives/banned-historical-archives6/main/'+fname,
            "sources": ["战地新歌"],
            "artists": [
            ],
            "art_forms": [
            ],
          },
        ],
        "lyricists": [
        ],
      },
    ],
    "composers": [
    ],
  },
  "version": 2,
}
            target = Path('../../../config/archives6/' + id +'.ts')
            with open(target, 'w') as f:
                f.write('export default ' + json.dumps(meta, indent=4, ensure_ascii=False))
            shutil.copy(os.path.join(current_directory, fname), '..')

