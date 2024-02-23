// 定义协议文件的路径
const PROTO_PATH = "./obei.proto";
// 引入 gRPC 和 proto-loader 模块
const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");
// 使用 proto-loader 加载协议文件
const packageDefinition = protoLoader.loadSync(PROTO_PATH);
// 使用 gRPC 加载协议包，并将其绑定到 obei 对象
const obei = grpc.loadPackageDefinition(packageDefinition).obei;

// 引入 isolated-vm 和 fs 模块
const ivm = require("isolated-vm");
const fs = require('fs');

// async 关键字表示这是一个异步函数
async function text(jscode) {
  // 创建一个新的 Isolate 实例。它是一个全新的 V8 实例，使用 128M 内存限制
  const isolate = new ivm.Isolate({ memoryLimit: 128 });
  // 创建一个新的上下文
  const context = await isolate.createContext();
  // CompileScriptSync 是 synchronous（同步）的函数，它会阻塞当前的事件循环直到脚本编译结束
  const script1 = isolate.compileScriptSync(jscode);
  // 在指定的上下文中执行一个脚本
  await context.eval('global = this');
  await script1.run(context);
  // 再次编译并运行一个脚本
  const script2 = isolate.compileScriptSync('getHK();');
  const result = await script2.run(context);
  console.log(result);
  return result;
}

// 定义一个函数读取一个文件，如果出错会打印错误信息
function readFileSync(filePath) {
  try {
    const data = fs.readFileSync(filePath, 'utf8');
    return data;
  } catch (err) {
    console.error(`Error reading file from disk: ${err}`);
  }
  return null;
}

// 调用一个异步函数 Funcobei
// call 是一个对象，包含了函数调用的相关信息，callback 是一个回调函数
async function Funcobei(call, callback) {
  // 创建一个新的 Isolate 实例
  let isolate = new ivm.Isolate({ memoryLimit: 128 });
  // 创建一个新的上下文
  let context = await isolate.createContext();
  // 读取指定的文件
  jsStr = readFileSync('./obei.js'); //call.request.jscode;
  // 同步编译一个脚本
  let script1 = isolate.compileScriptSync(jsStr);
  // 在指定的上下文中执行一个脚本
  await context.eval('global = this');
  await script1.run(context);
  console.log(call.request.jscode, call.request.cookie);
  // 编译并运行一个脚本，脚本中含有调用的参数
  let script2 = isolate.compileScriptSync(`GetHpM("${call.request.cookie}", "${call.request.jscode}");`);
  // 运行该脚本并获取结果
  let result = await script2.run(context);
  console.log(result);
  try {
    // 将结果返回给调用者
    callback(null, { message:  result });
  } catch (e) {
    callback({
      code: grpc.status.INVALID_ARGUMENT,
      details: "Invalid JS code",
    });
  }
}

// 创建一个新的 gRPC 服务器
const server = new grpc.Server();
// 为该服务器添加服务，其中 obei.Greeter.service 是服务的定义，Funcobei 是服务的实现
server.addService(obei.Greeter.service, {
  obeiHKIIUU9O618PPTHPM: Funcobei,
});

// 启动该服务器并使其开始监听
server.bindAsync(
  "0.0.0.0:50051",
  grpc.ServerCredentials.createInsecure(),
  (error, port) => {
    if (error) {
      console.error(error);
      process.exit(1);
    }
    console.log(`Server started, listening: 0.0.0.0:${port}`);
  }
);