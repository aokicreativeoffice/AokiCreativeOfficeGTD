module.exports = async () => {

if (window.mermaid) {

mermaid.initialize({

startOnLoad: true,

theme: "neutral",

themeVariables: {
fontSize: "12px"
},

flowchart: {
nodeSpacing: 25,
rankSpacing: 35,
padding: 4,
curve: "basis"
}

});

}

};