<template>
  <div>
    <h1>Add New Movie</h1>
    <form id="MovieForm" @submit.prevent="saveMovie">
      <div v-if="success" class="alert alert-success">
        Movie successfully added
      </div>
      <div v-if="errors.length" class="alert alert-danger">
        <ul>
          <li v-for="error in errors">{{ error }}</li>
        </ul>
      </div>
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" name="title" class="form-control" />
      </div>
      <div class="form-group mb-3">
        <label for="description" class="form-label">Movie Description</label>
        <textarea name="description" class="form-control"></textarea>
      </div>
      <div class="form-group mb-3">
        <label for="poster" class="form-label">Photo Upload</label>
        <input type="file" name="poster" class="form-control" />
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let success = ref(false);

let csrf_token = ref("");
let errors = ref([]);
let errorDisplayStatus = ref({});

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      csrf_token.value = data.csrf_token;
  })
}

onMounted(() => {
  getCsrfToken();
});

function validateForm() {
  errors.value = [];
  errorDisplayStatus.value = {};

  let titleInput = document.getElementsByName("title")[0];
  let descriptionInput = document.getElementsByName("description")[0];
  let fileInput = document.getElementsByName("poster")[0];

  if (!titleInput.value) {
    errors.value.push("Title is required");
  }

  if (!descriptionInput.value) {
    errors.value.push("Description is required");
  }

  if (!fileInput.value) {
    errors.value.push("File is required");
  }

  // Set errorDisplayStatus to false for each error that has not been displayed yet
  errors.value.forEach(error => {
    if (!errorDisplayStatus.value[error]) {
      errorDisplayStatus.value[error] = false;
    }
  });

  return errors.value.length === 0;
}

function saveMovie() {
  let MovieForm = document.getElementById('MovieForm');
  let form_data = new FormData(MovieForm);

  if (validateForm()) {
    fetch("/api/v1/movies", {
      method: 'POST',
      body: form_data,
      headers: {
        'X-CSRFToken': csrf_token.value
      }
    })
      .then(function (response) {
        if (response.ok) {
          success.value = true;
        } else {
          throw new Error('Failed to add movie');
        }
      })
      .catch(function (error) {
        console.log(error);
        errors.value.push("Accepted file format: jpg, png, jpeg)");
      });
  }
}
</script>
