# -*- coding: utf-8 -*-
import minium
import time


class FirstTest(minium.MiniTest):
    def test_get_system_info(self):
        sys_info = self.app.call_wx_method("getSystemInfo")
        b = self.page.get_element(".userinfo-nickname", text_contains="当").inner_text
        self.page.get_element(".userinfo-avatar").click()
        print(b)
        self.assertIn("SDKVersion", sys_info.result.result)
