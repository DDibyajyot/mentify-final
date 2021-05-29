import React, { useRef, useState } from 'react';
import './App.css';
import firebase from 'firebase/app';
import 'firebase/firestore';
import 'firebase/auth';

import { useAuthState } from 'react-firebase-hooks/auth';
import { useCollectionData } from 'react-firebase-hooks/firestore';

firebase.initializeApp({
  //your config
  apiKey: "AIzaSyBPmQCu83BJMRT5fwRivNHpZ5Su35u0_Ag",
  authDomain: "superchat-8ed3b.firebaseapp.com",
  projectId: "superchat-8ed3b",
  storageBucket: "superchat-8ed3b.appspot.com",
  messagingSenderId: "1010006230400",
  appId: "1:1010006230400:web:e57c8aa6e37ff89fea6d65",
  measurementId: "G-LF4W4JM5V3"
})

const auth = firebase.auth();
const firestore = firebase.firestore();

function App() {

  const [user] = useAuthState(auth);

  return (
    <div className="App">
      <header>

      </header>
      <section>
        {user ? <ChatRoom />: <SignIn />}
      </section>
    </div>
  );
}

export default App;

function SignIn() {
  const signInWithGoogle = () => {
    const provider = new firebase.auth.GoogleAuthProvider();
    auth.signInWithPopup(provider);
  }
  return(
    <button onClick={signInWithGoogle}>Sign In with Google</button>
  )
}

function SignOut() {
  return auth.currentUser && (

    <button onClick={()=> auth.signOut()}>Sign Out</button>
  )
}

function ChatRoom() {

  const dummy = useRef();
  
  const messagesRef = firestore.collection('messages');
  const query = messagesRef.orderBy('createdAt').limit(25);

  const [messages] = useCollectionData(query, {idField: 'id'});

  const [formValue, setFormValue] = useState('');

  const sendMessage = async(e) => {

    e.preventDefault();

    const { uid, photoURL } = auth.currentUser;

    await messagesRef.add({
      text: formValue,
      createdAt: firebase.firestore.FieldValue.serverTimestamp(), 
      uid,
      photoURL
    });

    setFormValue('');
    dummy.current.scrollIntoView({behaviour: 'smooth'});
  }

  return (
    <>
      <main>
        {messages && messages.map(msg => <ChatMessage key={msg.id} message={msg} />)}
        <div ref={dummy}></div>
      </main>

      <form onSubmit={sendMessage}>
        <input type="text" value={formValue} onChange={(e) => setFormValue(e.target.value)} placeholder="Say something nice"/>
        <button type = "submit">Submit</button>
      </form>

      <div>
        <SignOut />
      </div>  
    </>
  )
}

function ChatMessage(props) {
  const { text, uid, photoURL } = props.message;
  
  const messageClass = uid === auth.currentUser.uid ? 'sent': 'received';

  return (
    <div className={`message ${messageClass}`}>
      <img src={photoURL} />
      <p>{text}</p>
    </div>

  )
}