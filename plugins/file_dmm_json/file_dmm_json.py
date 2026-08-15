import orjson, re
from GalTransl import LOGGER
from GalTransl.GTPlugin import GFilePlugin


class file_plugin(GFilePlugin):
    def gtp_init(self, plugin_conf: dict, project_conf: dict):
        self.pname = plugin_conf["Core"].get("Name", "")
        settings = plugin_conf["Settings"]
        self.output_with_kv = settings.get("output_with_kv", True)
        self.remove_ruby_text = settings.get("remove_ruby_text", True)
        self.ruby_text_regex = settings.get("ruby_text_regex", "<ruby=.*?>(.*?)</ruby>")
        pass

    def load_file(self, file_path: str) -> list:
        if not file_path.endswith(".json"):
            raise TypeError("JSON file - 404 not found")
        with open(file_path, "r", encoding="utf-8") as f:
            json_list = orjson.loads(f.read())
        if self.output_with_kv:
            for i in json_list:
                i["src_msg"]=i["message"]
        if self.remove_ruby_text:
            for i in json_list:
                match = re.finditer(self.ruby_text_regex, i["message"])
                if match:
                    for x in match:
                        i["message"] = i["message"].replace(x.group(), x.groups()[0])
        return json_list

    def save_file(self, file_path: str, transl_json: list):
        if self.output_with_kv:
            kv = {}
            for tran in transl_json:
                kv[tran["src_msg"]] = tran["message"]
            with open(file_path, "wb") as f:
                f.write(orjson.dumps(kv, option=orjson.OPT_INDENT_2))
        else:
            with open(file_path, "wb") as f:
                f.write(orjson.dumps(transl_json, option=orjson.OPT_INDENT_2))

    def gtp_final(self):
        pass
