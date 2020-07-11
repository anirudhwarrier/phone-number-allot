do $$
begin
    if not exists(select 1 FROM pg_roles WHERE rolname='pna_admin') then
        CREATE ROLE pna_admin  CREATEDB CREATEROLE LOGIN PASSWORD 'pass';
    end if;
end
$$ language plpgsql;

CREATE ROLE pna_view   LOGIN PASSWORD 'pass';
CREATE ROLE pna_user   LOGIN PASSWORD 'pass';
