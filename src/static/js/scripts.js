async function buy(amount) {
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]");
  const creatorId = document.getElementById("creator_id").value;
  const email = document.getElementById("id_email").value;

  const formData = new FormData();
  formData.append("email", email);
  formData.append("creator_id", creatorId);
  formData.append("amount", amount);

  const response = await fetch("/api/create_support/", {
    method: "POST",
    headers: {
      "X-CSRFTOKEN": csrftoken,
    },
    body: formData,
  });

  const data = await response.json();
  console.log("data", data);
  window.location.href = data.url;
}
