window = {
  ActiveXObject: "",
  addEventListener: function (eventName, handler) {
    if (eventName === "beforeunload") {
      console.log("beforeunload event added");
      debugger;
      return;
    }
    // 对其他事件的处理
  },
  document: {
    documentElement: {
      getAttribute: function (attr) {
        // 不论attr的值是多少，都返回null
        return null;
      },
    },
  },
};
navigator = {
  userAgent:
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
};
window = self = top = global;

document = {
  cookie: "",
  documentElement: {
    getAttribute: function () {
      return;
    },
  },
  getElementById: function (id) {
    if (id == "iusa88fgfccmr00rPP") {
      return {
        content: "1708536190",
      };
    }
  },
  getElementsByTagName: function (name) {
    if (name == "head") {
      return head={
          accessKey: "",
          ariaAtomic: null,
          src: "https://ntp.msn.cn/Mcopss6d6w6EWERuu.js?fsdfs9g=95e28c9fdf3cb598bb8d265b1c03694e&rfgc8op=90121708614011.488&dsf2qePdfTY=JC11010",
        };
      
    }
  },
  compatMode: "CSS1Compat",
};

setInterval = function () {};

function getHK() {
  return document.cookie;
}
;;;;;;