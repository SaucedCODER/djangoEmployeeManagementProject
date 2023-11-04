
const toast = document.querySelector(".toastZ"),
alertMess = document.querySelector("#msg"),
closeIcon = document.querySelector(".close-toast"),
progress = document.querySelector(".progress");

let timer1, timer2;

  timer1 = setTimeout(() => {
      if(alertMess?.textContent.length > 0) {
          toast.classList.remove("active");
      }
  }, 5000); //1s = 1000 milliseconds

  timer2 = setTimeout(() => {
      if(alertMess?.textContent.length > 0) {
          progress.classList.remove("active");
      }
  }, 5300);

closeIcon?.addEventListener("click", () => {
  toast.classList.remove("active");
  
  setTimeout(() => {
    progress.classList.remove("active");
  }, 300);

  clearTimeout(timer1);
  clearTimeout(timer2);
});