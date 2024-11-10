# GalTransl For DMM Games

### 簡介

一個基於GalTransl的fork

主要針對DMM遊戲而改，但用法是一致的。(詳細用法請看[GalTransl](https://github.com/xd2333/GalTransl/blob/main/README.md))

大家都知道這些遊戲是持續性更新的。

當做這類遊戲劇情漢化時，往往需要持續更新遊戲檔案，然後也免不了拆包修改打包等繁複的程序。

為了迴避這些煩人的程序，我們可以採用注入方式以修改遊戲文本，從而達至同樣效果。

---

**雖然名叫GalTransl For DMM Games，但理論上，適合使用於其他遊戲。**

**此fork最終輸出結果為一個Key Value JSON，而不是name message格式的JSON**

```
{
    "こんにちは": "你好",
    "さようなら": "再見"
}
```

最後，你需要使用這個JSON以取代每一句遊戲文字

```python
import json

kv = json.loads('{"こんにちは": "你好", "さようなら": "再見"}')
text = "こんにちは"
if kv.get(text):
    text = text.replace("こんにちは", kv[text])
print(text)
```

#### 關於發佈方法

1. 放在本地
    1. 缺點；需要發佈更新檔
    2. 優點：省錢。
2. 租一個小型VPS，然後給其他玩家遠端讀取
    1. 優點：免除手動更新的煩惱，可以實時修改翻譯內容
    2. 缺點：每月有一筆額外開支

**關於Key Value JSON的使用/注入方式，請參考下方的實作例子**

### Config

| 欄位             | 預設值                      | 說明                                                                                                               |
|----------------|--------------------------|------------------------------------------------------------------------------------------------------------------|
| dmmGameMode    | true                     | 開啟/關閉DMM KV JSON 模式                                                                                              |
| removeRubyText | false                    | 開啟/關閉移除Ruby標籤功能                                                                                                  |
| rubyTextRegex  | `<ruby=.*?>(.*?)</ruby>` | Regexp正規表示式，只保留(.*?)內的文字<br/>預設是UTAGE3所使用的Ruby標籤<br/>例子：`<ruby=やくさい>厄災</ruby>`<br/>最後只保留`厄災`這個詞語                 |
| useLastName    | false                    | 是否只使用最後一個名稱為角色名稱<br/>某些遊戲文本可能存在多個名稱<br/>但只使用最後一個作為人名<br/>例子：`["声の低い警察官", "？？？"]`<br/>這時候就需要啟用此功能<br/>將人名鎖定為`？？？` |

### 實作

您可以參考這幾個實作以編寫自己的遊戲漢化/機翻mod。

| 遊戲名稱   | 注入工具    | Repo                                                            |
|--------|---------|-----------------------------------------------------------------|
| 閃耀之星騎士 | BepInEx | [TSKHook](https://github.com/TSKModding/TSKHook)                |
| 閃耀之星騎士 | Frida   | [TSKHook-frida](https://github.com/TSKModding/TSKHook-frida)    |
| 愛麗絲秘跡  | BepInEx | [IMYSHook](https://github.com/IrisMystery/IMYSHook)             |
| 愛麗絲秘跡  | Frida   | [IMYSHook-Frida](https://github.com/IrisMystery/IMYSHook-frida) |
| 少女藝術綺譚 | BepInEx | [GCMod](https://github.com/anosu/GCMod)                         |