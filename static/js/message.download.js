const sugesstion = document.querySelectorAll('.sugesstion')

sugesstion.forEach(element => {
    element.addEventListener('click', () => {
        domtoimage.toPng(element).then((data) => {
            let link = document.createElement("a")
            link.download = "my-funsta-new-post.png"
            link.href = data;
            link.click();
        })
    })
})

const messageimage = document.getElementById('message-image');

const QuestionConver = () => {
    messageimage.style.display = "block";
 
    setTimeout(() => {
        domtoimage.toPng(messageimage)
            .then((data) => {
                let link = document.createElement("a");
                link.download = "my-Question-answer.png";
                link.href = data;
                link.click();
            })
            .catch((error) => {
                console.error("Error generating the image:", error);
            })
            .finally(() => {
                messageimage.style.display = 'none';
            });
    }, 100); 
}
