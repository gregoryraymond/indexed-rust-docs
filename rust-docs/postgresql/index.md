# PostgreSQL 18 Documentation

> Source: https://www.postgresql.org/docs/current/

## Quick Reference

Comprehensive documentation for PostgreSQL, the world's most advanced open source relational database. Covers SQL, administration, programming interfaces, and internals.

## Table of Contents

### Preface

- [Preface](https://www.postgresql.org/docs/current/preface.html) - About this documentation
- [What is PostgreSQL?](https://www.postgresql.org/docs/current/intro-whatis.html) - Introduction
- [History of PostgreSQL](https://www.postgresql.org/docs/current/history.html) - Project history
- [Conventions](https://www.postgresql.org/docs/current/notation.html) - Documentation conventions
- [Further Information](https://www.postgresql.org/docs/current/resources.html) - Additional resources
- [Bug Reporting](https://www.postgresql.org/docs/current/bug-reporting.html) - How to report bugs

### Part I: Tutorial

- [1. Getting Started](https://www.postgresql.org/docs/current/tutorial-start.html) - Installation and basics
- [2. The SQL Language](https://www.postgresql.org/docs/current/tutorial-sql.html) - SQL fundamentals
- [3. Advanced Features](https://www.postgresql.org/docs/current/tutorial-advanced.html) - Views, foreign keys, transactions

### Part II: The SQL Language

- [4. SQL Syntax](https://www.postgresql.org/docs/current/sql-syntax.html) - SQL syntax fundamentals
- [5. Data Definition](https://www.postgresql.org/docs/current/ddl.html) - Tables, schemas, constraints
- [6. Data Manipulation](https://www.postgresql.org/docs/current/dml.html) - INSERT, UPDATE, DELETE
- [7. Queries](https://www.postgresql.org/docs/current/queries.html) - SELECT statements and joins
- [8. Data Types](https://www.postgresql.org/docs/current/datatype.html) - Numeric, string, date/time, JSON, arrays
- [9. Functions and Operators](https://www.postgresql.org/docs/current/functions.html) - Built-in functions
- [10. Type Conversion](https://www.postgresql.org/docs/current/typeconv.html) - Type casting and conversion
- [11. Indexes](https://www.postgresql.org/docs/current/indexes.html) - B-tree, hash, GiST, GIN indexes
- [12. Full Text Search](https://www.postgresql.org/docs/current/textsearch.html) - Text search features
- [13. Concurrency Control](https://www.postgresql.org/docs/current/mvcc.html) - MVCC and locking
- [14. Performance Tips](https://www.postgresql.org/docs/current/performance-tips.html) - Query optimization
- [15. Parallel Query](https://www.postgresql.org/docs/current/parallel-query.html) - Parallel execution

### Part III: Server Administration

- [16. Installation from Binaries](https://www.postgresql.org/docs/current/install-binaries.html) - Binary installation
- [17. Installation from Source](https://www.postgresql.org/docs/current/installation.html) - Compiling from source
- [18. Server Setup](https://www.postgresql.org/docs/current/runtime.html) - Starting and running the server
- [19. Server Configuration](https://www.postgresql.org/docs/current/runtime-config.html) - postgresql.conf settings
- [20. Client Authentication](https://www.postgresql.org/docs/current/client-authentication.html) - pg_hba.conf and auth methods
- [21. Database Roles](https://www.postgresql.org/docs/current/user-manag.html) - Users and permissions
- [22. Managing Databases](https://www.postgresql.org/docs/current/managing-databases.html) - CREATE/DROP database
- [23. Localization](https://www.postgresql.org/docs/current/charset.html) - Character sets and collation
- [24. Routine Maintenance](https://www.postgresql.org/docs/current/maintenance.html) - VACUUM, ANALYZE, REINDEX
- [25. Backup and Restore](https://www.postgresql.org/docs/current/backup.html) - pg_dump, pg_restore, PITR
- [26. High Availability](https://www.postgresql.org/docs/current/high-availability.html) - Replication and failover
- [27. Monitoring](https://www.postgresql.org/docs/current/monitoring.html) - Statistics and logging
- [28. Write-Ahead Log](https://www.postgresql.org/docs/current/wal.html) - WAL configuration and reliability
- [29. Logical Replication](https://www.postgresql.org/docs/current/logical-replication.html) - Publish/subscribe replication
- [30. JIT Compilation](https://www.postgresql.org/docs/current/jit.html) - Just-in-time compilation
- [31. Regression Tests](https://www.postgresql.org/docs/current/regress.html) - Testing PostgreSQL

### Part IV: Client Interfaces

- [32. libpq](https://www.postgresql.org/docs/current/libpq.html) - C library interface
- [33. Large Objects](https://www.postgresql.org/docs/current/largeobjects.html) - Binary large object support
- [34. ECPG](https://www.postgresql.org/docs/current/ecpg.html) - Embedded SQL in C
- [35. Information Schema](https://www.postgresql.org/docs/current/information-schema.html) - Standard metadata views

### Part V: Server Programming

- [36. Extending SQL](https://www.postgresql.org/docs/current/extend.html) - User-defined functions and types
- [37. Triggers](https://www.postgresql.org/docs/current/triggers.html) - Trigger functions
- [38. Event Triggers](https://www.postgresql.org/docs/current/event-triggers.html) - DDL event triggers
- [39. The Rule System](https://www.postgresql.org/docs/current/rules.html) - Query rewrite rules
- [40. Procedural Languages](https://www.postgresql.org/docs/current/xplang.html) - PL/pgSQL, PL/Python, etc.
- [41. PL/pgSQL](https://www.postgresql.org/docs/current/plpgsql.html) - PostgreSQL procedural language
- [42. PL/Tcl](https://www.postgresql.org/docs/current/pltcl.html) - Tcl procedural language
- [43. PL/Perl](https://www.postgresql.org/docs/current/plperl.html) - Perl procedural language
- [44. PL/Python](https://www.postgresql.org/docs/current/plpython.html) - Python procedural language
- [45. SPI](https://www.postgresql.org/docs/current/spi.html) - Server Programming Interface
- [46. Background Workers](https://www.postgresql.org/docs/current/bgworker.html) - Custom background processes
- [47. Logical Decoding](https://www.postgresql.org/docs/current/logicaldecoding.html) - Change data capture
- [48. Replication Progress](https://www.postgresql.org/docs/current/replication-origins.html) - Replication tracking
- [49. Archive Modules](https://www.postgresql.org/docs/current/archive-modules.html) - Custom archiving
- [50. OAuth Validators](https://www.postgresql.org/docs/current/oauth-validators.html) - OAuth authentication

### Part VI: Reference

- [SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html) - Complete SQL command reference
- [Client Applications](https://www.postgresql.org/docs/current/reference-client.html) - psql, pg_dump, createdb, etc.
- [Server Applications](https://www.postgresql.org/docs/current/reference-server.html) - postgres, initdb, pg_ctl, etc.

### Part VII: Internals

- [51. Overview](https://www.postgresql.org/docs/current/overview.html) - Architectural overview
- [52. System Catalogs](https://www.postgresql.org/docs/current/catalogs.html) - Internal system tables
- [53. System Views](https://www.postgresql.org/docs/current/views.html) - pg_stat_*, pg_tables, etc.
- [54. Frontend/Backend Protocol](https://www.postgresql.org/docs/current/protocol.html) - Wire protocol
- [55. Coding Conventions](https://www.postgresql.org/docs/current/source.html) - PostgreSQL coding standards
- [56. Native Language Support](https://www.postgresql.org/docs/current/nls.html) - Internationalization

### Part VIII: Appendices

- [A. Error Codes](https://www.postgresql.org/docs/current/errcodes-appendix.html) - Complete error code list
- [B. Date/Time Support](https://www.postgresql.org/docs/current/datetime-appendix.html) - Time zones and formats
- [C. SQL Keywords](https://www.postgresql.org/docs/current/sql-keywords-appendix.html) - Reserved words
- [D. SQL Conformance](https://www.postgresql.org/docs/current/features.html) - SQL standard compliance
- [E. Release Notes](https://www.postgresql.org/docs/current/release.html) - Version history
- [F. Additional Modules](https://www.postgresql.org/docs/current/contrib.html) - Extensions (pg_trgm, hstore, etc.)
- [G. Additional Programs](https://www.postgresql.org/docs/current/contrib-prog.html) - Utility programs
- [H. External Projects](https://www.postgresql.org/docs/current/external-projects.html) - Third-party tools
- [I. Source Repository](https://www.postgresql.org/docs/current/sourcerepo.html) - Git repository
- [J. Documentation](https://www.postgresql.org/docs/current/docguide.html) - Writing documentation
- [K. Limits](https://www.postgresql.org/docs/current/limits.html) - PostgreSQL limits
- [L. Acronyms](https://www.postgresql.org/docs/current/acronyms.html) - Abbreviations glossary
- [M. Glossary](https://www.postgresql.org/docs/current/glossary.html) - Term definitions
- [N. Color Support](https://www.postgresql.org/docs/current/color.html) - Terminal colors
- [O. Obsolete Features](https://www.postgresql.org/docs/current/appendix-obsolete.html) - Deprecated features

## Common Queries → Documentation

| Query/Task | Section | URL |
|------------|---------|-----|
| How do I get started? | Tutorial | https://www.postgresql.org/docs/current/tutorial-start.html |
| How do I create tables? | Data Definition | https://www.postgresql.org/docs/current/ddl.html |
| How do I query data? | Queries | https://www.postgresql.org/docs/current/queries.html |
| How do I create indexes? | Indexes | https://www.postgresql.org/docs/current/indexes.html |
| How do I configure the server? | Server Configuration | https://www.postgresql.org/docs/current/runtime-config.html |
| How do I backup and restore? | Backup and Restore | https://www.postgresql.org/docs/current/backup.html |
| How do I set up replication? | High Availability | https://www.postgresql.org/docs/current/high-availability.html |
| How do I optimize queries? | Performance Tips | https://www.postgresql.org/docs/current/performance-tips.html |
| How do I write functions? | PL/pgSQL | https://www.postgresql.org/docs/current/plpgsql.html |
| How do I manage users? | Database Roles | https://www.postgresql.org/docs/current/user-manag.html |
