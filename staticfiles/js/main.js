 const carousel = document.getElementById('carousel');
    const track = document.getElementById('track');
    let isDragging = false;
    let startX;
    let scrollStart;

    carousel.addEventListener('pointerdown', (e) => {
      isDragging = true;
      startX = e.clientX;
      scrollStart = carousel.scrollLeft;
      carousel.style.cursor = 'grabbing';
    });

    carousel.addEventListener('pointermove', (e) => {
      if (!isDragging) return;
      const dx = e.clientX - startX;
      carousel.scrollLeft = scrollStart - dx;
      updateAngles();
    });

    carousel.addEventListener('pointerup', () => {
      isDragging = false;
      carousel.style.cursor = 'grab';
    });

    carousel.addEventListener('pointerleave', () => {
      isDragging = false;
      carousel.style.cursor = 'grab';
    });

    function updateAngles() {
      const items = track.querySelectorAll('.carousel-item');
      const center = window.innerWidth / 2;
      items.forEach(item => {
        const rect = item.getBoundingClientRect();
        const offset = rect.left + rect.width / 2 - center;
        const angle = offset / 25;
        const scale = 1 - Math.abs(offset) / 1000;
        item.style.setProperty('--angle', `${angle}deg`);
        item.style.setProperty('--scale', scale);
      });
    }

    window.addEventListener('resize', updateAngles);
    carousel.addEventListener('scroll', updateAngles);
    updateAngles();

//Rating

document.querySelectorAll('.rating-form').forEach(form => {
  const stars = form.querySelectorAll('.star');
  const ratingInput = form.querySelector('input[name="rating"]');

  stars.forEach(star => {
    star.addEventListener('click', () => {
      const value = star.getAttribute('data-value');
      ratingInput.value = value;

      stars.forEach(s => s.classList.remove('selected'));
      for (let i = 0; i < value; i++) {
        stars[i].classList.add('selected');
      }
    });
  });

 form.addEventListener('submit', function(e) {
  e.preventDefault();

  const movieId = form.getAttribute('data-movie-id');
  const rating = ratingInput.value;
  const comment = form.querySelector('textarea[name="comment"]').value.trim();
  const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value;

  console.log("Submitting comment:", comment); // ✅ Confirm it's captured

  fetch(`/reviews/submit/${movieId}/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken
    },
    body: JSON.stringify({ rating: rating, comment: comment })
  })
  .then(response => {
    if (response.ok) {
      alert('Thanks for rating!');
      form.reset(); // Optional: clear form after submission
    } else {
      alert('Something went wrong.');
    }
  })
  .catch(error => {
    console.error("Error submitting review:", error);
    alert("Submission failed.");
  });
});
 });


//svg
const svgs = document.querySelectorAll('.bg-svg');
let current = 0;

setInterval(() => {
  const next = (current + 1) % svgs.length;

  // Start fading in the next SVG *before* fading out the current
  svgs[next].classList.add('active');

  // Delay removal of current to allow overlap
  setTimeout(() => {
    svgs[current].classList.remove('active');
    current = next;
  }, 500); // overlap duration (adjust if needed)
}, 8000); // every 8 seconds
