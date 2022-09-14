// in src/admin/App.jsx
import * as React from "react";
import { Admin, Resource, ListGuesser } from 'react-admin';
// import jsonServerProvider from 'ra-data-json-server';
import simpleRestProvider from 'ra-data-simple-rest';

const dataProvider = simpleRestProvider('http://0.0.0.0:8000/api');

function MyAdmin({ Component, pageProps }) {
  if (typeof window === "object")
    return (
      <Admin dataProvider={dataProvider}>
        <Resource name="users" list={ListGuesser} />
      </Admin>
    );
  else
    return null
}

export default MyAdmin;