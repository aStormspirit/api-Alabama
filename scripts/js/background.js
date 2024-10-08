var config = {
  mode: "fixed_servers",
  rules: {
    singleProxy: {
      scheme: "http",
      host: "81.215.152.137",
      port: parseInt("8403"),
    },
    bypassList: ["localhost"],
  },
};

chrome.proxy.settings.set({ value: config, scope: "regular" }, function () {});

function callbackFn(details) {
  return {
    authCredentials: {
      username: "user210318",
      password: "u9bkcx",
    },
  };
}

chrome.webRequest.onAuthRequired.addListener(
  callbackFn,
  { urls: ["<all_urls>"] },
  ["blocking"]
);
