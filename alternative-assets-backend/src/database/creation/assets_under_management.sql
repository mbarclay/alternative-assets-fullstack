create table asset_classes
(
    asset_class_code TEXT not null
        constraint asset_classes_pk
            primary key,
    asset_class      TEXT not null
);

create table countries
(
    iso  TEXT(3) not null
        constraint countries_pk
            primary key,
    name TEXT
);

create table investory_types
(
    investory_type_code TEXT not null
        constraint investory_types_pk
            primary key,
    investory_type      TEXT not null
);

create table investors
(
    investor_code       TEXT    not null
        constraint investors_pk
            primary key,
    name                TEXT    not null,
    added_epoch        integer not null,
    last_updated_epoch   integer not null,
    country_iso         integer not null
        constraint investors_countries_iso_fk
            references countries,
    investory_type_code TEXT    not null
        constraint investors_investory_types_investory_type_code_fk
            references investory_types
);

create table commitments
(
    commitment_uuid  TEXT    not null
        constraint commitments_pk
            primary key,
    investor_code    TEXT    not null
        constraint commitments_investors_investor_code_fk
            references investors,
    asset_class_code TEXT    not null
        constraint commitments_asset_classes_asset_class_code_fk
            references asset_classes,
    currency_code    TEXT    not null,
    amount           integer not null
);

create index commitments_asset_class_code_index
    on commitments (asset_class_code);

create index commitments_currency_code_index
    on commitments (currency_code);

create index commitments_investor_code_index
    on commitments (investor_code);
