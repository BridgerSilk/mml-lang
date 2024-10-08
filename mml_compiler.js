const fs = require('fs');

function convertMMLToHTML(mmlContent) {
    mmlContent = mmlContent.replace(/doc!.mml/g, '<!DOCTYPE html>');
    mmlContent = mmlContent.replace(/\(&([a-zA-Z0-9]+)((\s+[a-zA-Z]+!"[^"]*")*)\)/g, '<$1$2>');
    mmlContent = mmlContent.replace(/\.&([a-zA-Z0-9]+)/g, '</$1>');
    mmlContent = mmlContent.replace(/([a-zA-Z]+)!"([^"]+)"/g, '$1="$2"');
    mmlContent = mmlContent.replace(/[{}]/g, '');

    // Special syntax handling
    mmlContent = mmlContent.replace(/<mml>/g, '<html>');
    mmlContent = mmlContent.replace(/<mml/g, '<html');
    mmlContent = mmlContent.replace(/<\/mml>/g, '</html>');
    mmlContent = mmlContent.replace(/<text>/g, '<p>');
    mmlContent = mmlContent.replace(/<text/g, '<p');
    mmlContent = mmlContent.replace(/<\/text>/g, '</p>');
    mmlContent = mmlContent.replace(/link="([^"]+)"/g, 'href="$1"');

    return mmlContent;
}

function compileMMLToHTML(inputFile, outputFile) {
    fs.readFile(inputFile, 'utf8', (err, mmlContent) => {
        if (err) {
            console.error(err);
            return;
        }
        let htmlContent = convertMMLToHTML(mmlContent);
        htmlContent = htmlContent.replace(/\n\s*\n/g, '\n');
        fs.writeFile(outputFile, htmlContent, 'utf8', (err) => {
            if (err) console.error(err);
            else console.log(`Successfully converted ${inputFile} to ${outputFile}`);
        });
    });
}

const inputMMLFileName = process.argv[2];
if (inputMMLFileName) {
    const inputMMLFile = `${inputMMLFileName}.mml`;
    const outputHTMLFile = `${inputMMLFileName}.html`;
    compileMMLToHTML(inputMMLFile, outputHTMLFile);
} else {
    console.log("Please provide a valid .mml file name (without suffix).");
}