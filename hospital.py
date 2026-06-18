import streamlit as st
import pandas as pd
import pickle

st.cache_resource
def load_mode():
  with open('hospital_mode.pk1', 'rb') as f:
    return pickle .load(f)

bundle = load_model()

model = bundle['model']
scaler = bundle['scaler']
features = bundle['features']
cols_to_scale = bundle['cols_to_scale']
dept_map_inv = bundle['dept_map_inv']
gender_map = bundle['gender_map']
temp_map = bundle['temp_map']
hr_map = bundle['hr_map']
dur_map = bundle['dur_map']
cc_map = bundle['cc_map']

DEPT_INFO = (
  'Respiratory Meidcine' : {
    'icon': '💨',
  'color': '#05afed'
  'desc':'Specialty in conditionss affecting the lungs and always'
   'step': ['Visit level 2, wing B', 'Estimated wait: 15-25 min', 'please wear mask']
  },
   },
    'Cardiology': {
        'icon': '❤️', 'color': '#dc2626',
        'desc': 'Specialises in heart and cardiovascular conditions.',
        'steps': ['Visit Level 3, Wing A', 'Estimated wait: 20–30 min', 'Bring any previous ECG reports'],
    },
    'Gastroenterology': {
        'icon': '🫃', 'color': '#d97706',
        'desc': 'Specialises in digestive system and abdominal conditions.',
        'steps': ['Visit Level 1, Wing C', 'Estimated wait: 10–20 min', 'Avoid eating before consultation'],
    },
    'Neurology': {
        'icon': '🧠', 'color': '#7c3aed',
        'desc': 'Specialises in brain, spine, and nervous system conditions.',
        'steps': ['Visit Level 4, Wing A', 'Estimated wait: 25–35 min', 'Bring list of current medications'],
    },
    'General Medicine': {
        'icon': '🩺', 'color': '#059669',
        'desc': 'Handles general health concerns and non-specialist conditions.',
        'steps': ['Visit Level 1, Wing A', 'Estimated wait: 10–15 min', 'Registration desk is open 24/7'],
    },
    'Dermatology': {
        'icon': '🔬', 'color': '#b45309',
        'desc': 'Specialises in skin, hair, and nail conditions.',
        'steps': ['Visit Level 2, Wing D', 'Estimated wait: 15–20 min', 'Bring photos of affected area if possible'],
    },
}
