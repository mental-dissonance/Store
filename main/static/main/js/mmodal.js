const modal = document.querySelector(".modal");
const modal_enter = document.querySelector(".modal_enter");
const modal_reg = document.querySelector(".modal_reg");

const overlay = document.querySelector(".overlay");
const openModalBtn = document.querySelector(".enter");
const closeModalBtns = document.querySelectorAll(".modal-close");
const openRegBtn = document.querySelector(".modal-reg");

const openModal = function () {
    modal.classList.remove("hidden");
    modal_enter.classList.remove("hidden");
    overlay.classList.remove("hidden");
    document.body.style.position = 'fixed';
    document.body.style.top = `-${window.scrollY}px`;
};

const openReg = function() {
    modal_enter.classList.add("hidden");
    modal_reg.classList.remove("hidden");
}

openModalBtn.addEventListener("click", openModal);

const closeModal = function () {
    modal.classList.add("hidden");
    modal_enter.classList.add("hidden");
    modal_reg.classList.add("hidden");
    overlay.classList.add("hidden");
    const scrollY = document.body.style.top;
    document.body.style.position = '';
    document.body.style.top = '';
    window.scrollTo(0, parseInt(scrollY || '0') * -1);
};

openRegBtn.addEventListener("click", openReg);

overlay.addEventListener("click", closeModal);
closeModalBtns .forEach(function(btn) {
    btn.addEventListener("click", closeModal);
});