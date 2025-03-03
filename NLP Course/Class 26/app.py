import os
import tempfile
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from llama_index.core import SimpleDirectoryReader


def plot_image(image):
    st.image(image, use_container_width=True)


def get_response_from_image(image, prompt, api_key):
    with tempfile.TemporaryDirectory() as tmpdir:
        image_file_path = os.path.join(tmpdir, "uploaded_image.png")
        image.save(image_file_path)

        image_documents = SimpleDirectoryReader(tmpdir).load_data()
        openai_mm_model = OpenAIMultiModal(
            model="gpt-4o", api_key=api_key, max_new_tokens=3000
        )

        response = openai_mm_model.complete(
            prompt=prompt,
            image_documents=image_documents,
        )

        print(response)

        if hasattr(response, 'text'):
            return response.text

        if hasattr(response, 'message'):
            return response.message

        return "No response found"


def main():
    st.title("Image Questioning AI")  # Fixed: changed st.main to st.title
    api_key = st.text_input("Enter your OpenAI API key: ", type="password")

    if api_key:
        uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])  # Fixed: file_upload to file_uploader

        if uploaded_image:
            image = Image.open(uploaded_image)  
            plot_image(image)
            
            prompt = st.text_area("Ask a question about the image: ", placeholder="e.g. What is this image about?")

            if st.button("Get response"): 
                if prompt: 
                    with st.spinner("Generating response..."): 
                        response = get_response_from_image(image, prompt, api_key)

                    st.subheader("Response: ")
                    st.write(response)

                else:
                    st.warning("Please enter a prompt before generating a response")

            if st.button("Clear"):
                st.cache_data.clear()


if __name__ == "__main__":
    main()