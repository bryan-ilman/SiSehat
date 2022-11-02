function show() {
    // getPenyakit();
    getObat();
}

// function getPenyakit() {
//     var listPasien = document.getElementById("daftar-pasien");
//     var pasien = listPasien.options[listPasien.selectedIndex].text;
//     console.log("in getPenyakit");
//         $.ajax({
//             type: "GET",
//             url: "/dokter/riwayat-penyakit/" + pasien
//         }).done((data) => {
//             console.log("about to showPenyakit")
//             showPenyakit(data)
//         });
// }

// function showPenyakit(pasien) {
//     const table = $('.display');
//     table.empty();
//     table.append(
//         `<tr class="table-header">
//         <th>Nama Penyakit</th>
//         <th>Tanggal Diagnosis</th>
//         <th>Pesan Dokter</th>
//         <th>Sembuh</th>
//         </tr>`
//     )
//     pasien.forEach(penyakit => {
//         const penyakitData = `
//         <tr>
//             <th>${penyakit.fields.nama_penyakit}</th>
//             <th>${penyakit.fields.tanggal_diagnosis}</th>
//             <th>${penyakit.fields.deskripsi_keluhan}</th>
//             <th>
//             <button id="penyakit-toggle" onclick=togglePenyakit(${penyakit.pk})>${penyakit.fields.sembuh ? "&#9989" : "&#10060"}</button>
//             </th>
//         </tr>`;
//         table.append(penyakitData);
//     })
// }

function addObat() {
    console.log("in addObat");
    var listPasien = document.getElementById("daftar-pasien");
    var pasien = listPasien.options[listPasien.selectedIndex].text;
    const form = $('.new-obat');
    $.ajax({
        type: "POST",
        url: "/dokter/add-obat/" + pasien,
        data: form.serialize(),
        error: console.log("error"), 
    }).done(function (data) {
        console.log("about to getObatDokter");
        form.trigger("reset");
        getObatDokter();
    })
    $("#staticBackdrop").modal("hide");
}

function getObatDokter() {
    var listPasien = document.getElementById("daftar-pasien");
    var pasien = listPasien.options[listPasien.selectedIndex].text;
    console.log("in getObatDokter");
        $.ajax({
            type: "GET",
            url: "/obat/get-obat/" + pasien
        }).done((data) => {
            console.log("about to showObat")
            showObat(data)
        });
}

function getObatPasien() {
    console.log("in getObatPasien");
        $.ajax({
            type: "GET",
            url: "/obat/get-obat/"
        }).done((data) => {
            console.log("about to showObat")
            showObat(data)
        });
}

function showObat(data_obat) {
    const table = $('.display-keluhan');
    table.empty();
    table.append(
        `<tr class="table-header">
        <th>Tanggal</th>
        <th>Nama Obat</th>
        <th>Deskripsi</th>
        </tr>`
    )
    data_obat.forEach(obat => {
        const dataObat = `
        <tr>
            <th>${obat.fields.tanggal}</th>
            <th>${obat.fields.nama_obat}</th>
            <th>${obat.fields.deskripsi}</th>
        </tr>`;
        table.append(dataObat);
    })
}

